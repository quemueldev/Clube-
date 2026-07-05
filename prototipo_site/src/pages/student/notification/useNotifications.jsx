import { useState } from "react"
import { get_invitations } from "../../../infra/api/manager/tools"

export default function useNotifications(){
    const [myInvitation, setMyInvitation] = useState(null)

    const _getMyInvitation = (user, invitations)=>{
        const myInvitation = invitations.find((invitation)=>{
            return invitation.student_id === user.id
        })
        setMyInvitation(myInvitation || null)
    }
    const getInvitations = async(user)=>{
        const [err, resp] = await get_invitations()
        const invitations = resp.data?.invitations || []
        _getMyInvitation(user, invitations)
        return [err, resp]
    }
    return {
        myInvitation,
        getInvitations,
    }
}