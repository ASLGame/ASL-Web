import * as React from 'react'
import {Li, Brand, Navbar, Ul, Ur, Dropdown, DropCont} from "./NavBar.styled.js"
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
            <span>...</span>
            <DropCont>
              <p>Test</p>
            </DropCont>
          </Dropdown>
        </Ur>
        <div />
    </Navbar>
  )
};

export default NavBar;