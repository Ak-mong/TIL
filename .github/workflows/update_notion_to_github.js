const { Client } = require('notion-sdk-node');
const { promises: fs } = require('fs');

const notion = new Client({ auth: process.env.NOTION_API_TOKEN });
const databaseId = 'YOUR_NOTION_DATABASE_ID'; // Notion에서 가져온 데이터베이스 ID로 대체

async function fetchNotionContent() {
  const response = await notion.databases.query({
    database_id: databaseId,
  });

  // 여기에서 Notion 데이터를 가져와서 필요한 형식으로 변환

  return transformedData;
}

async function updateGitHub(content) {
  // 여기에서 GitHub 저장소에 업데이트된 내용을 푸시

  await fs.writeFile('path/to/updated/file.md', content);
}

async function run() {
  const notionContent = await fetchNotionContent();
  const transformedContent = transformData(notionContent);
  await updateGitHub(transformedContent);
}

run().catch(error => console.error(error));
