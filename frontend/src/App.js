import './App.css';
import { BrowserRouter, Route, Routes } from 'react-router-dom';
import HomePage from './pages/HomePage';
import LoginPage from "./pages/LoginPage";
import RegisterPage from './pages/RegisterPage';
import LogoutPage from './pages/LogoutPage';
import ResetPage from './pages/ResetPassword';


function App() {
  return (
    <div className="App">
      <BrowserRouter>
        <Routes>
          <Route path='/home' element={<HomePage />}></Route>
          <Route path='/login' element={<LoginPage />}></Route>
          <Route path='/register' element={<RegisterPage />}></Route>
          <Route path='/logout' element={<LogoutPage />}> </Route>
          <Route path='/password-reset/:encoded_pk/:token' element={<ResetPage />}> </Route>
        </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
