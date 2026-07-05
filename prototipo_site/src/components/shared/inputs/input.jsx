import styles from './input.module.css'

export default function MyInput({title, value, onChange}){
    return(
        <input 
        className={styles.input}
        type="text" 
        value={value}
        onChange={(e) => onChange(e.target.value)}
        placeholder={title}
        />
    )
}