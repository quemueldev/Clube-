import { authApi, handleRequest } from "../client";

export const Test = async () => {
  return handleRequest(() => authApi.get("manager/test/"));
};

export const get_invitations = async ()=>{
  return handleRequest(() => authApi.get("manager/invitations/")) 
}