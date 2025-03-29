export default function appendToEachArrayValue(array, appendString) {
  const newArray = [];

  for (let idx = 0; idx < array.length; idx++) {
    newArray[idx] = appendString + array[idx];
  }

  return newArray;
}
