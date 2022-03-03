import styled from "styled-components";

export const Button = styled.button`
    // background-color: var(--pinkred);
    border: 2px solid #000000;
    box-sizing: border-box;
    border-radius: 23px;
    width: 100%;
    padding-left: 20%;
    padding-right: 20%;
    cursor: pointer;
    &:hover {
        opacity: 0.8;
        trasnform: scale(0.80);
    }
    background-image: linear-gradient(to right, var(--pinkred) , var(--pink));
`