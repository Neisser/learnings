import fs from 'fs/promises';

async function getNum(filename) {
  return parseInt(await fs.readFile(filename, 'utf-8'), 10);
}

try {
  const numberPromises = [1, 2, 3].map(i => getNum(`${i}.txt`));

  const numbers = await Promise.all(numberPromises);

  console.log(numbers[0] + numbers[1] + numbers[2]);

} catch (err) {
  console.error('something went wrong');
  console.error(err);
}