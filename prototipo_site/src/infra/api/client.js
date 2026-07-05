import axios from "axios";

export const api = axios.create({
  baseURL: "http://localhost:3000/api/",
  withCredentials:true
})
export const authApi = axios.create({
  baseURL: "http://localhost:3000/api/",
  withCredentials:true
})



export const handleRequest = async (func) => {
    try{
        const data = await func()
        return [null, data]
    } catch(error){
       console.log("ERRO:", error.response?.data)
       console.log('aqui: ', JSON.stringify(error.response?.data, null, 2))
        return [_get_error(error), null]
    }
    
}
//criar interceptor na api
export const _get_error = (error) => {
  if (error?.response) {
    const data = error.response.data;
    console.log(data)

    return {
      erro:
        data?.detail ||
        data?.message ||
        data?.error ||
        JSON.stringify(data) ||
        "Erro na requisição",
    };
  }

  return {erro: error?.message || "Erro desconhecido",};
};
