import { parse } from 'yaml';

// Bundle local YAML at build time; keep the existing editing/import workflow.
const sources = import.meta.glob<string>('../../_data/*.yaml', {
  query: '?raw', import: 'default', eager: true,
});
export function loadData(name: string) {
  return parse(sources[`../../_data/${name}.yaml`]);
}
export const info = loadData('main_info');
export const profile = loadData('profile');
export const papers = loadData('publications').papers;
export const media = loadData('research_media');
export const venues = loadData('publication_venues');
export const experiences = loadData('experience').experiences;
export const awards = loadData('awards').awards;
export const patents = loadData('patents').patents;
