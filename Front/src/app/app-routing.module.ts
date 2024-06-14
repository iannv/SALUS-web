import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { NosotrosComponent } from './pages/nosotros/nosotros.component';
import { ContactoComponent } from './pages/contacto/contacto.component';
import { RegistroComponent } from './pages/registro/registro.component';
import { LoginComponent } from './pages/login/login.component';
import { SuscripcionComponent } from './ecommerce/suscripcion/suscripcion.component';
import { FormComponent } from './ecommerce/form/form.component';
import { FormEditComponent } from './ecommerce/form-edit/form-edit.component';
import { CuentaComponent } from './pages/cuenta/cuenta.component';
import { SuscripcionAdminComponent } from './ecommerce/suscripcion-admin/suscripcion-admin.component';
import { PacienteComponent } from './pages/paciente/paciente.component';
import { PagoComponent } from './ecommerce/pago/pago.component';
import { PagoAdminComponent } from './ecommerce/pago-admin/pago-admin.component';
import { PagoClienteComponent } from './ecommerce/pago-cliente/pago-cliente.component';
import { EspecialidadComponent } from './pages/especialidad/especialidad.component';
import { DetalleEspecialidadComponent } from './pages/detalle-especialidad/detalle-especialidad.component';
import { ProfesionalesComponent } from './pages/profesionales/profesionales.component';
import { CProfesionalComponent } from './pages/components/c-profesionales/c-profesionales.component';
import { ProtegidosModule } from './protegidos/protegidos.module';
import { UserProfileComponent } from './protegidos/pages/user-profile/user-profile.component';
import { AuthGuard } from './pages/login/auth.guard';
import { EditarPerfilComponent } from './protegidos/pages/editar-perfil/editar-perfil.component';
import { TurnoDetailComponent } from './pages/turno/turno-detail/turno-detail.component';
import { FormEspecialidadComponent } from './pages/especialidad/form-especialidad/form-especialidad.component';
import { EditEspecialidadComponent } from './pages/especialidad/edit-especialidad/edit-especialidad.component';
import { Pagina404Component } from './pages/pagina404/pagina404.component';

const routes: Routes = [
  {path:'home', component:HomeComponent,
    /* children:[
      {path:'home',component: UserProfileComponent},
      {path:'home',component: ConsultaComponent},
    ] */
  },
  {path: '', redirectTo: '/home', pathMatch: 'full'},
  {path:'servicios', component:EspecialidadComponent},
  {path:'detalle-servicio/:id', component: DetalleEspecialidadComponent},
  {path:'agregar-servicio', component: FormEspecialidadComponent},
  {path:'editar-servicio/:id', component: EditEspecialidadComponent},
  {path:'nosotros', component:NosotrosComponent},
  {path:'contacto', component:ContactoComponent},
  {path:'registro', component:RegistroComponent},
  {path:'pago', component:PagoComponent},
  {path:'login', component:LoginComponent},
  {path:'paciente', component:PacienteComponent},
  {path:'profesionales',component:ProfesionalesComponent},
  {path:'cprofesionales',component:CProfesionalComponent},
  { path: 'user-profile/:id', component: UserProfileComponent, canActivate: [AuthGuard] },
  { path: 'editar-perfil/:id', component: EditarPerfilComponent, canActivate: [AuthGuard] },
  { path: 'detalle-turno/:id', component: TurnoDetailComponent, canActivate: [AuthGuard] },
  // {path:'suscripcion', component:SuscripcionComponent},
  // {path:'formSuscripcion', component:FormComponent},
  // {path:'formSuscripcionEdit', component:FormEditComponent},
  // {path:'cuenta', component:CuentaComponent},
  // {path:'adminSuscripcion', component:SuscripcionAdminComponent},
  // {path:'adminPago', component:PagoAdminComponent},
  // {path:'clientePago', component:PagoClienteComponent},
  {path:'**', component:Pagina404Component},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule,ProtegidosModule]
})

export class AppRoutingModule { }
