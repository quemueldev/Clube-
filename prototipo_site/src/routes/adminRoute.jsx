import { useEffect, useState } from "react";
import { Navigate, Outlet } from "react-router-dom";
import useGetClub from "../pages/student/home/useHome"; // Ajuste o caminho do seu hook

export default function AdminRoute() {
    const { call, userIsAdmin, err } = useGetClub();
    const [loading, setLoading] = useState(true);

    useEffect(() => {
        const verifyAccess = async () => {
            await call();
            setLoading(false);
        };
        verifyAccess();
    }, []);

    // Enquanto está buscando os dados do usuário/clube, exibe um loading
    if (loading) {
        return <div>Carregando...</div>; // Ou um componente de Spinner/Loading bem bonito
    }

    // Se houve erro ou o usuário não for admin, chuta ele para a página inicial (ou login)
    if (err || !userIsAdmin) {
        return <Navigate to="/home" replace />;
    }

    // Se passou em tudo, dá acesso às rotas filhas
    return <Outlet />;
}