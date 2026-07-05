import { useEffect, useState } from "react";
import { Navigate, Outlet } from "react-router-dom";

import { Test } from "../infra/api/manager/tools";


export default function  ManagerRoute(){
    const [loading, setLoading] = useState(true);
    const [isManager, setIsManager] = useState(false);

    useEffect(() => {
        const load = async()=>{
            try{
            // eslint-disable-next-line no-unused-vars
            const [err, resp] = await Test()
            if (!err) setIsManager(true)
            else setIsManager(false)
            }finally{
            setLoading(false)
            }
        }
        load()
    }, []);
    if (loading) return <p>Carregando...</p>;
    return isManager ? <Outlet /> : <Navigate to="/home" replace />;
}