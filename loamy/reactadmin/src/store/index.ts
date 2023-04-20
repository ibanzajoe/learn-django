import { BehaviorSubject } from "rxjs";

export interface Pokemon {
	id: number;
	name: string;
	type: string[];
	hp: number;
	attack: number;
	defense: number;
	special_attack: number;
	special_defense: number;
	speed: number;
}

export const rawPokemon$ = new BehaviorSubject<Pokemon[]>([]);

fetch('/pokemon-simplified.json')
    .then(res => res.json())
    .then(data => {
        console.log('hello');
        rawPokemon$.next(data)
    })