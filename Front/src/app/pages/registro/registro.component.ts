import { Component, OnInit } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import {Router} from '@angular/router';
import { RegistryService } from 'src/app/services/auth/registry.service';
import { HttpClient } from '@angular/common/http';
import { RegistryRequest } from "../../services/auth/registryRequest";
import { SharedServicesComponent } from 'src/app/services/auth/shared-services/shared-services.component';

@Component({
  selector: 'app-registro',
  templateUrl: './registro.component.html',
  styleUrls: ['./registro.component.css']
})
export class RegistroComponent implements OnInit{
  
  loginError:string="";
  pacienteData: any = {};
  registryForm=this.formBuilder.group({
    Nombre_UP:['', Validators.required],
    Apellido_UP:['', Validators.required],
    Email_UP:['', [Validators.required,Validators.email]],
    Clave_UP:['',Validators.required],
  })
  

  constructor(private formBuilder:FormBuilder, private registryService: RegistryService, private router:Router, private sharedService: SharedServicesComponent){}
  
  ngOnInit(): void{}

  registry(){
    if(this.registryForm.valid){
      this.registryService.checkEmail().subscribe(data => {
        const email = data.find(paciente => paciente.Email_UP === this.registryForm.value.Email_UP)
        if (email) {
          alert("Ya existe ese email. Ingrese uno nuevo")
        } else {
          this.registryService.createUser(this.registryForm.value as RegistryRequest).subscribe(data => {
            this.router.navigateByUrl('/home');
            this.sharedService.isRegistered = true;
            this.pacienteData = data;
            localStorage.setItem('pacienteData', JSON.stringify(this.pacienteData));
        })
        }
      })
    }
    
   /*  if(this.registryForm.valid){
      this.registryService.createUser(this.registryForm.value as RegistryRequest).subscribe(data => {
        console.log(data)
        this.router.navigateByUrl('/home');
        this.sharedService.isRegistered = true;
        this.pacienteData = data;
        localStorage.setItem('pacienteData', JSON.stringify(this.pacienteData));
      })

    }  */
  }
}