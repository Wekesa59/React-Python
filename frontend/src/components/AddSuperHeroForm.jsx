import React, { useState } from "react";

const AddSuperHeroForm = ({addSuperHero}) => {
    const [superHeroName, setSuperHeroName] = useState("");

    const handleSubmit = (event) => {
        event.preventDefault();
        if (superHeroName)
        {
            addSuperHero( superHeroName );
            setSuperHeroName("");
        }
    };

    return (
        <form onSubmit={handleSubmit}>
            <input
                type="text"
                value={superHeroName}
                onChange={(e) => setSuperHeroName(e.target.value)}
                placeholder="Enter superhero name"
            />
            <button type="submit">Add SuperHero</button>
        </form>
    );
};

export default AddSuperHeroForm;