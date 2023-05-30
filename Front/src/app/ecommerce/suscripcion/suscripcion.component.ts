import { Component, OnInit } from '@angular/core';
import { SuscriptionService } from './../../services/suscription.service'
import { Suscription } from 'src/app/model/suscription.model';

@Component({
  selector: 'app-suscripcion',
  templateUrl: './suscripcion.component.html',
  styleUrls: ['./suscripcion.component.css']
})
export class SuscripcionComponent implements OnInit{

  mySuscriptions: Suscription[] = [];
 myServices: Suscription["descripcion"] = [];


  choseSuscription: {} = {};

  constructor(private suscriptionService: SuscriptionService){
  }

  ngOnInit(): void {
    this.suscriptionService.getAllSuscriptions()
    .subscribe(data => {
      this.mySuscriptions = data
      console.log(this.mySuscriptions)
    })
  }

  getSuscription(){
    console.log(this.mySuscriptions)
  }



  getSuscriptionOne(){
    let id = 3
    this.suscriptionService.getSuscription(id)
    .subscribe(data => {
      this.choseSuscription = data;
      console.log(this.choseSuscription)
    })
  }

}
