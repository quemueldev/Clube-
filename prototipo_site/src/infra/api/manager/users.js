import { authApi, handleRequest } from "../client";

export const getUsers =async()=>{
    return handleRequest(() => authApi.get("manager/users/"))
}