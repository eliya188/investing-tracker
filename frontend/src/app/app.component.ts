import { Component, OnInit } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterOutlet } from '@angular/router';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [CommonModule, RouterOutlet],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent implements OnInit {
  squares: { delay: string}[] = [];
  title = 'frontend';

  ngOnInit(): void {
    for (let i = 0; i < 20; i++) {
      this.squares.push({ delay: `${Math.random() * 2}s` });
    }
  }
}
