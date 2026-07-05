import { useEffect } from "react"
import useGetClub from "./useHome"
import styles from './home.module.css'
import { useNavigate } from "react-router-dom"



function Home(){
    const controller = useGetClub() 
    const navigate = useNavigate()
    useEffect(()=>{
        const load = async()=>{
            await controller.call()
        }
        load()
    }, [])
    return (
        <>
        <h1>Home do aluno</h1>
        <p>rota do aluno</p>
        {controller.err && <p>erro: {controller.err}</p>}
        
        {controller.clubs.map((club)=>{
            return (
                <div 
                key={club.id} 
                className={styles.clubCard} 
                onClick={()=> navigate(`/club/${club.id}`)}>
                    <h3>Clube</h3>
                    <p>Titulo: {club.name}</p>
                    
                </div>
            )
        })}
       
        <p>meu user: {controller.user ? controller.user.name : 'carregando'}</p>
        
        {controller.userIsAdmin && (
            <button onClick={()=> navigate(`/my_club/${controller.idClubAdmin}`)}>meu clube clube</button>
        )}

        <button onClick={() => navigate('/notifications')}>notificações</button>
        
        
        </>
    )
}
export default Home