import { useNavigate } from 'react-router-dom'
import MyInput from '../../../components/shared/inputs/input'
import styles from './login.module.css'
import { useLogin } from './useLogin'


function Login(){
    const navigate = useNavigate()
    const controller = useLogin()
    const handleLogin=async()=>{
        // eslint-disable-next-line no-unused-vars
        const [err,resp] = await controller.doRequest()
        if (!err) navigate('/home_manager')
    }
    
    
    return(
        <div className={styles.container}>
            <MyInput 
            title={'matricula:'}
            value={controller.enrollment}
            onChange={controller.setEnrollment}
            />
            <p>separar</p>
            <MyInput 
            title={'senha:'}
            value={controller.password}
            onChange={controller.setPassword}
            />
            <button
            onClick={async()=> handleLogin()}
            >
                enviar
            </button>
            
        </div>
    )
}
export default Login