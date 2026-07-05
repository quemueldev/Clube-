import { authApi, handleRequest } from "../client";

export const Test = async () => {
  return handleRequest(() => authApi.get("manager/test/"));
};
export const sendInvitation = async (id)=>{
    return handleRequest(() => authApi.post('manager/send_invitation/', {
      id: id
    }))
}