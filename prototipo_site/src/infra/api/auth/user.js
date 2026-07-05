import { api, authApi, handleRequest } from "../client";

export const Login = async (data) => {
  return handleRequest(() => api.post("users/login_web/", data));
};
export const register= async (data)=>{
    return await handleRequest(() => api.post("users/sign_in/",data))
}
//dps enviar pelo headers #ajeitar a api tbm
export const getUser =async () =>{
  return handleRequest(() => authApi.get('users/get_user/'))
}