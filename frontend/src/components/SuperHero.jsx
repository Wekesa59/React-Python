import React, { useEffect, useState } from "react";
import api from "../api";
import AddSuperheroForm from "./AddSuperoForm";

const SuperHeroList = () => {
    const [superheroes, setSuperheroes] = useState([]);

    const fetchSuperheroes = async () => {
        try {
            const response = await api.get("/superheroes");
            setSuperheroes(response.data.superheroes);
        } catch (error) {
            console.error("Error fetching superheroes:", error);
        }
    };

    const addSuperHero = async (superhero) => {
        try {
            await api.post("/superheroes", superhero);
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
            <AddSuperheroForm addSuperHero={addSuperHero} />
            <ul>
                {superheroes.map((superhero) => (
                    <li key={superhero.id}>{superhero.name}</li>
                ))}
            </ul>
        </div>
    );
};

export default SuperHeroList;