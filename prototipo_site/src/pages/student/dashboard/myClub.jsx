import { useParams } from "react-router-dom"
import useGetClub from "../home/useHome"
import { useEffect } from "react"
import DaysSelector from "../../../components/selectors/selector"

function MyClub(){
    const {id }= useParams()
    const controller = useGetClub()
        useEffect(()=>{
            const load = async()=>{
                await controller.getClub(id)
            }
            load()
        }, [])
    return (
        <div>
            <h1>Meu Clube</h1>
        <p>rota clube por id: {id}</p>
        <h2>titulo: {controller.club?.name}</h2>
        <h3>descrição: {controller.club?.description}</h3>
        <h3>dono: {controller.club?.student?.first_name}</h3>
        <h3>dias de atividade: {controller.club?.activity_days.join(', ')}</h3>
        <h3>desde: {controller.club?.created_at?.split('T')[0]}</h3>
       
        <h1>area de updates</h1>
        <DaysSelector/>
        
        </div>
    )
}
export default MyClub