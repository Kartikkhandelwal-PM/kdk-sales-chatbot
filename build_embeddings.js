/**
 * build_embeddings.js
 * Run once to embed all KB articles and save to embeddings.json
 * Usage: node build_embeddings.js
 *
 * Cost: ~$0.003 total for all 287 articles (text-embedding-3-small)
 */

require('dotenv').config();
const OpenAI = require('openai');
const fs = require('fs');
const path = require('path');

if (!process.env.OPENAI_API_KEY) {
  console.error('❌  OPENAI_API_KEY not found. Copy .env.example to .env and add your key.');
  process.exit(1);
}

const openai   = new OpenAI({ apiKey: process.env.OPENAI_API_KEY });
const KB_DIR   = path.join(__dirname, '..', 'Knowledge Base Files');
const OUT_FILE = path.join(__dirname, 'embeddings.json');

function parseArticles(text, product) {
  const articles = [];
  const parts = text.split(/\n(?=#### \d+\.)/);
  for (const part of parts) {
    const titleMatch = part.match(/#### \d+\.\s*(.+)/);
    if (!titleMatch) continue;
    const title    = titleMatch[1].trim();
    const tagsMatch = part.match(/\*\*Tags:\*\*\s*(.+)/);
    const tags     = tagsMatch ? tagsMatch[1] : '';
    articles.push({ product, title, tags, content: part.trim() });
  }
  return articles;
}

function buildEmbedText(art) {
  // Title and tags carry the most signal; include first 1200 chars of content for steps context
  const preview = art.content.slice(0, 1200).replace(/\*\*Tags:\*\*.+/, '').trim();
  return `Product: Express ${art.product}\nTitle: ${art.title}\nKeywords: ${art.tags}\n\n${preview}`;
}

async function embedBatch(texts) {
  const res = await openai.embeddings.create({
    model: 'text-embedding-3-small',
    input: texts,
  });
  return res.data.sort((a, b) => a.index - b.index).map(d => d.embedding);
}

async function main() {
  console.log('='.repeat(55));
  console.log('KDK KB — RAG Embedding Builder');
  console.log('='.repeat(55));

  let articles = [];
  for (const [file, product] of [
    ['Express-GST-KnowledgeBase.md', 'GST'],
    ['Express-TDS-KnowledgeBase.md', 'TDS'],
    ['Express-ITR-KnowledgeBase.md', 'ITR'],
  ]) {
    const text   = fs.readFileSync(path.join(KB_DIR, file), 'utf-8');
    const parsed = parseArticles(text, product);
    articles.push(...parsed);
    console.log(`✅  ${product}: ${parsed.length} articles`);
  }
  console.log(`\n📚  Total articles to embed: ${articles.length}`);

  const texts = articles.map(buildEmbedText);

  const BATCH = 50;
  const allEmbeddings = [];
  for (let i = 0; i < texts.length; i += BATCH) {
    const batch = texts.slice(i, i + BATCH);
    const batchNum = Math.floor(i / BATCH) + 1;
    const total    = Math.ceil(texts.length / BATCH);
    process.stdout.write(`\r   Embedding batch ${batchNum}/${total}...`);
    const embs = await embedBatch(batch);
    allEmbeddings.push(...embs);
    if (i + BATCH < texts.length) await new Promise(r => setTimeout(r, 150));
  }
  console.log('\n');

  const output = articles.map((art, i) => ({
    product:   art.product,
    title:     art.title,
    tags:      art.tags,
    content:   art.content,
    embedding: allEmbeddings[i],
  }));

  fs.writeFileSync(OUT_FILE, JSON.stringify(output));

  const sizeMB = (fs.statSync(OUT_FILE).size / 1024 / 1024).toFixed(2);
  console.log(`✅  Saved ${output.length} embeddings → embeddings.json (${sizeMB} MB)`);
  console.log('\n   Now restart the server: npm start');
}

main().catch(err => {
  console.error('\n❌  Error:', err.message);
  process.exit(1);
});
