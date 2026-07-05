import { Navigate, Outlet } from "react-router-dom";
import { check_login } from "../infra/api/student/users";

import { useEffect, useState } from "react";


export default function PrivateRoute() {
    const [loading, setLoading] = useState(true);
    const [authenticated, setAuthenticated] = useState(false);

    useEffect(() => {
        async function verify() {
            const [err, resp] = await check_login();

            if (!err && resp) {
                setAuthenticated(true);
            }

            setLoading(false);
        }

        verify();
    }, []);

    if (loading) {
        return <p>Carregando...</p>;
    }

    if (!authenticated) {
        return <Navigate to="/" replace />;
    }

    return <Outlet />;
}