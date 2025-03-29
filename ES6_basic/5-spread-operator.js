export default function concatArrays(array1, array2, string) {
  const stringToConcat = typeof string === 'string' ? string : '';
  return [...array1, ...array2, ...stringToConcat];
}
