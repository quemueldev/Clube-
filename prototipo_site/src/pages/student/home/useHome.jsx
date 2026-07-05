import { useState } from "react"
import { get_club, get_clubs } from "../../../infra/api/student/clubs"
import { get_user } from "../../../infra/api/student/users"

export default function useGetClub(){
    const [userIsAdmin, setUserIsAdmin] = useState(false)
    const [idClubAdmin, setIdClubAdmin] = useState(null)
    const [clubs, setClubs] = useState([])
    const [club, setClub] = useState()
    const [user, setUser]= useState()
    const [err, setErr] = useState()

    const getClub = async(id)=>{
        const [err, resp] = await get_club(id)
        if (!err) setClub(resp.data)
        else setErr(err)
    }
    const _loadClubs = async ()=>{
        const [err, resp] = await get_clubs()
        if (!err) {
            setClubs(resp.data)
            return resp.data
        }
        else {
            setErr(err)
            return null
        }
    }
    const _getUser = async ()=>{
        const [err, resp] = await get_user()
        if (!err) {
            setUser(resp.data) 
            return resp.data
        } 
        else {
            setErr(err)
            return null
        }
    }
    const _getValidation = (clubs, user)=>{
        const othersClubs = clubs.filter((club)=> {
            return club.student.id !== user.id
        })
        const userClub = clubs.find((club)=>{
            return club.student.id === user.id
        })
        setIdClubAdmin(userClub?.id || null)
        setClubs(othersClubs)
        setUserIsAdmin(!!userClub)
    }
    const call = async ()=>{
        const clubs = await _loadClubs()
        const user = await _getUser()
        if (clubs && user) {
            _getValidation(clubs, user)
        }
    }
    return {
        getClub,
        _getUser,
        call,
        clubs,
        club,
        user,
        err,
        userIsAdmin,
        idClubAdmin
    }
}