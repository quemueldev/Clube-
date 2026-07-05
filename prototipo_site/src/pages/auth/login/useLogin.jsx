import { useState } from "react"
import { Login } from "../../../infra/api/auth/user"


export const useLogin=()=>{
    const [enrollment, setEnrollment] = useState('')
    const [password, setPassword] = useState('')

    const doRequest = async()=>{
        const [err, resp]= await Login({
            enrollment: enrollment,
            password: password
        })
        if (!err) localStorage.setItem('access', resp.data.access)
        return [err,resp]
    }
    return {
        doRequest,
        enrollment, setEnrollment,
        password, setPassword
    }
}