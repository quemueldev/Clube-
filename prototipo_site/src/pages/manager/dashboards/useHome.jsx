import { useState } from "react";
import { getUsers } from "../../../infra/api/manager/users.js"
import { sendInvitation } from "../../../infra/api/manager/clubs.js";

export default function useHomeManager(){
    const [users, setUsers] = useState([]);
    const [loading, setLoading] = useState(false);
    const [error, setError] = useState(null);



    const loadUsers = async()=>{
        setLoading(true)
        setError(null)
        const [err, resp] = await getUsers()
        if (err) {setError(err)} 
        else {
            setUsers(Array.isArray(resp.data) ? resp.data: [])
        }
        setLoading(false)
    }
    const sendToStudent = async(id)=>{
        const [err, resp] = await sendInvitation(id)
        return [err, resp]
    }
    return {
        users,
        loading,
        error,
        loadUsers,
        sendToStudent
    }
}