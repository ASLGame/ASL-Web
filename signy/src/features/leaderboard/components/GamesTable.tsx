import styles from "./GamesTable.module.css"
import { useEffect, useState } from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";
import { Overall } from "./components/Overall";
import { Game1, Game2 } from "./components/Game";

export function ByGames(){
    const [tabIndex, setTabIndex] = useState(0);
    return(
        <div className={styles.container}>
            <Tabs className={styles.tab_container} selectedIndex={tabIndex} onSelect={(indx) => setTabIndex(indx)}>
                <TabList className={styles.tab_list}>
                    <Tab selectedClassName={styles.tab_selected} className={styles.tab}>Overall</Tab>
                    <Tab selectedClassName={styles.tab_selected} className={styles.tab}>Game 1</Tab>
                    <Tab selectedClassName={styles.tab_selected} className={styles.tab}>Game 2</Tab>
                </TabList>
                <TabPanel className={styles.tab_panel}>
                    <h2 style={{paddingBottom: "30px"}}>Highest Overall Scores</h2>
                    <Overall />
                </TabPanel>
                <TabPanel className={styles.tab_panel}>
                    <h2 style={{paddingBottom: "30px"}}>Game 1</h2>
                    <Game1 />
                </TabPanel>
                <TabPanel className={styles.tab_panel}>
                    <h2 style={{paddingBottom: "30px"}}>Game 2</h2>
                    <Game2 />
                </TabPanel>
            </Tabs>
        </div>
    );
}