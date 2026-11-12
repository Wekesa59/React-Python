import React, { useEffect, useState } from "react";
import AddSuperHeroForm from "./AddSuperHeroForm";
import api from "../api";

const SuperHeroList = () => {
    const [superheroes, setSuperheroes] = useState([]);

    const fetchSuperheroes = async () => {
        try {
            const response = await api.get("/superHeroes");
            setSuperheroes(response.data.superHeroes);
        } catch (error) {
            console.error("Error fetching superheroes:", error);
        }
    };

    const addSuperHero = async (superHeroName) => {
        try {
            await api.post("/superHeroes", { name: superHeroName });
            fetchSuperheroes();
        } catch (error) {
            console.error("Error adding superhero:", error);
        }
    };

    useEffect(() => {
        fetchSuperheroes();
    }, []);

    return (
        <div>
            <h2> Superhero List</h2>
            <ul>
                {superheroes.map((superHero, index) => (
                    <li key={index}>{superHero.name}</li>
                ))}
            </ul>
            <AddSuperHeroForm addSuperHero={addSuperHero} />
        </div>
    );
};

export default SuperHeroList;