import { api, handleRequest } from "../client"



export const get_clubs= async()=>{
    return await handleRequest(() => api.get("clubs/club/"))
}
export const get_club= async(id)=>{
    return await handleRequest(() => api.get(`clubs/get_club/${id}`))
}

export const updateDescription =async(newDes)=>{
    return await handleRequest(() => api.patch('clubs/alter_description/', {
        newDes
    }))
}
export const updateDays = async(newDays)=>{
    return await handleRequest(() => api.patch('clubs/add_days/', {
        days:newDays
    }))
}