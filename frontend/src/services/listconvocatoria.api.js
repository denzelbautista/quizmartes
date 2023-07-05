import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/convocatorias";

export const listConvoc = async () => {
  try {
    const { data } = await axios.get(BASE_URL);
    console.log("convocatorias.api.js: ", data);
    return data;
  } catch (error) {
    console.log("error here: ", error);
    throw error;
  }
};
