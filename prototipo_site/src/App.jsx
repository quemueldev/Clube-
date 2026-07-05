
import { Route, Routes } from 'react-router-dom'
import Login from './pages/auth/login/login'
import HomeManager from './pages/manager/dashboards/home'
import ManagerRoute from './routes/managerRoute'
import AdminRoute from './routes/adminRoute'
import Home from './pages/student/home/home'
import Club from './pages/student/clubs/club'
import MyClub from './pages/student/dashboard/myClub'
import PrivateRoute from './routes/loginRoute'
import Notification from './pages/student/notification/notification'

function App() {

  return (
    <Routes>
      <Route path='/' element={<Login/>}/>
      <Route element={<PrivateRoute />}>
        <Route path='/home' element={<Home/>}/>
        <Route path='/club/:id' element={<Club/>}/>
        <Route path='/notifications' element={<Notification/>}/>
      </Route>
      

      <Route element={<AdminRoute />}>
        <Route path='/my_club/:id' element={<MyClub/>}/>
      </Route>
      
      <Route element={<ManagerRoute />}>
        <Route path='/home_manager' element={<HomeManager/>}/>
      </Route>
    </Routes>
  )
}
export default App