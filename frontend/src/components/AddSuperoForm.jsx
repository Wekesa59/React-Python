import React, { useState } from "react";

const AddSuperheroForm = ({addSuperHero}) => {
    const [superheroName, setSuperheroName] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        if (superheroName)
        {
            addSuperHero({ name: superheroName });
            setSuperheroName("");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={superheroName}
                onChange={(e) => setSuperheroName(e.target.value)}
                placeholder="Enter superhero name"
            />
            <button type="submit">Add Superhero</button>
        </form>
    );
}