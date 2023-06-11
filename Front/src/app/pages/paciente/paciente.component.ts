/* import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import {Router} from '@angular/router';


@Component({
  selector: 'app-paciente',
  templateUrl: './paciente.component.html',
  styleUrls: ['./paciente.component.css']
})
export class PacienteComponent implements OnInit {
  apiUrl = '/api/v1/usuariospacientes/';

  constructor(private http: HttpClient, private router:Router) { }
  pacienteData: any = {};

  ngOnInit() {
    const pacienteDataString = localStorage.getItem('pacienteData');
    if (pacienteDataString) {
      this.pacienteData = JSON.parse(pacienteDataString);
      this.cargarPaciente();
    }
  }

  cargarPaciente() {
    if (this.pacienteData.id) {
      const url = `${this.apiUrl}${this.pacienteData.id}`;
      this.http.get<any>(url).subscribe(data => {
        this.pacienteData = data;
        console.log('Paciente cargado:', data);
      });
    }else{
      console.log('id undefined')
    }
  }

  actualizarPaciente() {
    const url = `${this.apiUrl}/${this.pacienteData.id}/`;
    this.http.put<any>(url, this.pacienteData).subscribe(response => {
      console.log('Paciente actualizado:', response);
    });
  }

  eliminarPaciente() {
    const url = `${this.apiUrl}/${this.pacienteData.id}/`;
    this.http.delete<any>(url).subscribe(response => {
      localStorage.removeItem('pacienteData');
      console.log('Paciente eliminado:', response);
      this.router.navigateByUrl('/home');
    });
  }
} */

import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { FormGroup, FormBuilder } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-paciente',
  templateUrl: './paciente.component.html',
  styleUrls: ['./paciente.component.css']
})
export class PacienteComponent implements OnInit {
  apiUrl = '/api/v1/usuariospacientes/';
  formulario!: FormGroup;

  pacienteData: any = {};

  constructor(private http: HttpClient, private formBuilder: FormBuilder, private router: Router) { }

  ngOnInit() {
    this.formulario = this.formBuilder.group({
      name: [''],
      lastName: [''],
      email: [''],
      age: [''],
      dni: [''],
      obraSocial: [''],
      medicoCabecera: [''],
      localidad: ['']
    });

    const pacienteDataString = localStorage.getItem('pacienteData');
    if (pacienteDataString) {
      this.pacienteData = JSON.parse(pacienteDataString);
      this.cargarPaciente();
    }
  }

  cargarPaciente() {
    if (this.pacienteData.id) {
      const url = `${this.apiUrl}${this.pacienteData.id}`;
      this.http.get<any>(url).subscribe(data => {
        this.pacienteData = data;
        console.log('Paciente cargado:', data);


        this.formulario.patchValue({
          name: this.pacienteData.Nombre_UP,
          lastName: this.pacienteData.Apellido_UP,
          email: this.pacienteData.Email_UP,
          age: this.pacienteData.age,
          dni: this.pacienteData.Dni_UP,
          obraSocial: this.pacienteData.obraSocial,
          medicoCabecera: this.pacienteData.medicoCabecera,
          localidad: this.pacienteData.localidad
        });
      });
    } else {
      console.log('id undefined');
    }
  }


  actualizarPaciente() {
    const valores = this.formulario.value;
    this.pacienteData = {
      ...this.pacienteData,
      ...valores
    };

    const url = `${this.apiUrl}/${this.pacienteData.id}/`;
    this.http.put<any>(url, this.pacienteData).subscribe(response => {
      console.log('Paciente actualizado:', response);
    });
  }

  eliminarPaciente() {
    const url = `${this.apiUrl}/${this.pacienteData.id}/`;
    this.http.delete<any>(url).subscribe(response => {
      localStorage.removeItem('pacienteData');
      console.log('Paciente eliminado:', response);
      this.router.navigateByUrl('/home');
    });
  }
}
