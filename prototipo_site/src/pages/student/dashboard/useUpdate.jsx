import { useState } from "react"
import { updateDescription as updateDesRequest, updateDays as updateDaysRequest } from "../../../infra/api/student/clubs"

export default function useUpdateClub(){
    const [newDes, setNewDes] = useState('')
    


    const updateDescription = async()=>{
        const [err, resp] = await updateDesRequest(newDes)
        return [err, resp]
    }
    const updateDays = async(days)=>{
        console.log(days)
        const [err, resp] = await updateDaysRequest(days)
        return [err, resp]
    }


    return {
        updateDescription,
        updateDays,
        setNewDes,
        newDes,
    }
}