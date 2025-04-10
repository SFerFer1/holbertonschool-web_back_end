function getFullResponseFromAPI(works) {
    return new Promise((resolve, reject) => {
      if (works) {
        resolve({
          status: 200,
          body: 'Success'
        });
      } else {
        reject({
          message: 'The fake API is not working currently'
        });
      }
    });
  }


  export default getFullResponseFromAPI;