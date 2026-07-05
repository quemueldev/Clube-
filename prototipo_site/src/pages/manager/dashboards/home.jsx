import { useEffect } from "react"
import useHomeManager from "./useHome"
import styles from './home.module.css'



function HomeManager(){
    const controller = useHomeManager()
    useEffect(() =>{
        const load = async ()=>{
            await controller.loadUsers()
        }
        load()
    }, [])

    if (controller.loading) return <p> Carregando usuarios...</p>
    if (controller.error) return <p>Ocorreu um erro {controller.error}</p>
    
    return (
        <>
        <p>rota protegida</p>
        <header>
            <nav>

            </nav>
        </header>
        <main>
            <section className={styles.studentSection}>
                <h1>Alunos: </h1>
                <ul>
            {controller.users.map((user)=>{
                return (
                    <li key={user.id}>
                        nome : {user.first_name}, <br />
                        matricula : {user.enrollment} <br />
                        aluno: {user.role} <br />
                        <button onClick={async()=>controller.sendToStudent(user.id)}>mandar form</button>
                    </li>
                )
            })}
        </ul>
            </section>
        </main>

        
        </>
    )
}
export default HomeManager