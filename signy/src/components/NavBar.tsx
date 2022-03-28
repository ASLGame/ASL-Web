import * as React from 'react'
import {Li, Brand, Navbar, Ul, Ur, Dropdown, DropCont, Input} from "./NavBar.styled.js"
import { useAppDispatch, useAppSelector } from "../app/hooks";
import { selectUser } from "../features/signin/signinSlice"; //use to check if user is signed in
import {ReactComponent as Signy} from "./signy.svg"



const NavBar = (props: {
    brand : { name: string; to: string};
    links : Array<{ name: string; to: string }>
}) => {
    const user = useAppSelector(selectUser)
    const { brand, links } = props;
    const NavLinks: any = () => links.map((link: { name: string, to: string }) => {
      if(!user && link.name=="Account"){
        return [<Li key="Sign-In"><a href="/signin">Sign-In</a></Li>, <Li key="Sign-Up"><a href="/signup">Sign-Up</a></Li>];
      }else{
        return <Li key={link.name}><a href={link.to}>{link.name}</a></Li>
      }});
    var DropLinks: any = () => {
      const links = [<a href="/">Leaderboards</a>, <p></p>, <a href="/">About Us</a>]
      if(user){
        return [links, <p></p>, <a href="/">Sign-Out</a>];
      }else{
        return links;
      }
    }
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
              <DropLinks />
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