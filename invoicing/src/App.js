import './App.css';
import {BrowserRouter, Routes, Route} from "react-router-dom"
import InvoiceList from './components/InvoiceList/InvoiceList';
import InvoiceForm from "./components/InvoiceForm/InvoiceForm";
import InvoiceItems from "./components/InvoiceItems/InvoiceItems";
import ItemForm from "./components/ItemForm/ItemForm";
import SignUp from './components/Signup/Signup';
import Login from './components/Login/Login';
import ProtectRoutes from './components/Routes/ProtectRoutes';

function App() {
  return (
    <div className="App">
      <BrowserRouter>
      <Routes>
        <Route path='/' element={<ProtectRoutes Component={ InvoiceList } />}>
        </Route>
        <Route path='newInvoice' element={<ProtectRoutes Component={ InvoiceForm } />}>
        </Route>
        <Route path='/:id' element={<ProtectRoutes Component={ InvoiceItems } />}>
        </Route>
        <Route path='/:id/newItem' element={<ProtectRoutes Component={ ItemForm } />}>
        </Route>
        <Route path='/signup' element={<SignUp />}>
        </Route>
        <Route path='/login' element={<Login />}>
        </Route>
      </Routes>
      </BrowserRouter>
    </div>
  );
}

export default App;
