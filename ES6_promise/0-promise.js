export function emptyPromise() {
  return new Promise((resolve) => {
    resolve();
  });
}
