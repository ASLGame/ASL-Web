import styles from "./GamesTable.module.css"
import { useState } from "react";
import { Tab, Tabs, TabList, TabPanel } from "react-tabs";

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
            </Tabs>
        </div>
    );
}