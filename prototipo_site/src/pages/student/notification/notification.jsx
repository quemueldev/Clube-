import { useEffect } from "react"
import useGetClub from "../home/useHome"
import useNotifications from "./useNotifications"

export default function Notification(){
    const {user, _getUser} = useGetClub()
    const { getInvitations, myInvitation } = useNotifications()
    useEffect(() => {
        _getUser();
    }, []);

    useEffect(() => {
        if (user && user.id) {
            getInvitations(user);
        }
    }, [user]);
    return(
        <>
        <h1>Notificações</h1>
        <p>Olá, {user?.name}!</p>

        {myInvitation ? (
            <p>tem que fazer o formulario aqui</p>
        ):(
            <p>não tem convite</p>
        )}
        </>
    )
}