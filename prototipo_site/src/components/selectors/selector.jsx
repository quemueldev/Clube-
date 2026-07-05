import { useState } from "react";
import useUpdateClub from "../../pages/student/dashboard/useUpdate";
// Importe seu hook 'useUpdateClub' do caminho correto
// import useUpdateClub from "./useUpdateClub"; 
import styles from './selector.module.css';


export default function DaysSelector() {
    const controller = useUpdateClub();
    const [selectedDays, setSelectedDays] = useState([]);

    const toggleDay = (day) => {
        if (selectedDays.includes(day)) {
            setSelectedDays(selectedDays.filter(d => d !== day)); // Remove se já existia
        } else {
            setSelectedDays([...selectedDays, day]); // Adiciona se não existia
        }
    };

    const handleSend = async () => {
        await controller.updateDays(selectedDays);
    };

    const daysOfWeek = [
        { id: 'segunda', label: 'Segunda' },
        { id: 'terca', label: 'Terça' },
        { id: 'quarta', label: 'Quarta' },
        { id: 'quinta', label: 'Quinta' },
        { id: 'sexta', label: 'Sexta' },
    ];

    return (
        <div style={{ display: 'flex', gap: '8px' }}>
            {daysOfWeek.map((day) => (
                <button
                    key={day.id}
                    onClick={() => toggleDay(day.id)}
                    className={selectedDays.includes(day.id) ? styles['btn-active'] : styles['btn']}
                >
                    {day.label}
                </button>
            ))}

            <button onClick={handleSend} style={{ fontWeight: 'bold' }}>
                Enviar
            </button>
        </div>
    );
}