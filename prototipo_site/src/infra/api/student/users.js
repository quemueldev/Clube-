import { api, handleRequest } from "../client"


export function get_user(){
    return handleRequest(()=> api.get('users/get_user/'))
}

export function check_login(){
    return handleRequest(()=> api.get('users/check_login/'))
}