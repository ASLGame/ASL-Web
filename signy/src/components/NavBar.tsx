import * as React from 'react'
import {Li, Brand, Navbar, Ul, Ur, Dropdown, DropCont, Input} from "./NavBar.styled.js"
import {ReactComponent as Signy} from "./signy.svg"



const NavBar = (props: {
    brand : { name: string; to: string};
    links : Array<{ name: string; to: string }>
}) => {
    const { brand, links } = props;
    const NavLinks: any = () => links.map((link: { name: string, to: string }) => <Li key={link.name}><a href={link.to}>{link.name}</a></Li>);
  return (
    <Navbar>
        <Ul>
          <Signy />
          <Brand href={brand.to}>{brand.name}</Brand>
        </Ul>
        <Ur>
          <NavLinks />
          <Dropdown>
            <Input type="button" id="..." onClick={() => dropdown()} value="..."/>
            <DropCont id="content">
              <a href="/">Leaderboards</a>
              <p></p>
              <a href="/">About Us</a>
            </DropCont>
          </Dropdown>
        </Ur>
        <div />
        
    </Navbar>
    
  )
};

function dropdown(){
  let content = document.getElementById("content");
  if(content){
    if(window.getComputedStyle(content).getPropertyValue("display") === "none"){
      content.style.display = "block";
    }else if(content?.style.display === "block"){
      content.style.display = "none";
    }
  }
}

export default NavBar;