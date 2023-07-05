import axios from "axios";

const BASE_URL = "http://127.0.0.1:5002/convocatorias";

export const registerConvoc = async (convoc) => {
  try {
    const { data } = await axios.post(BASE_URL, convoc);
    console.log("data: ", data);
  } catch (error) {
    console.log("error here: ", error);
    throw error;
  }
};
