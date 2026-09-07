import { Info } from 'lucide-react'
import type { ReactNode } from 'react'

export function InfoTooltip({ children, label }: { children: ReactNode; label: string }) {
  return <span className="group relative inline-flex align-middle"><button type="button" aria-label={label} className="inline-flex h-4 w-4 items-center justify-center rounded-full text-slate-400 outline-none transition-colors hover:text-slate-600 focus-visible:text-slate-700"><Info size={14} strokeWidth={1.9} /></button><span role="tooltip" className="pointer-events-none absolute left-0 top-full z-[1100] mt-2 w-64 origin-top-left border border-[#dfe1dc] bg-[#fffefa] px-3 py-2 text-left text-xs font-normal leading-5 text-slate-600 opacity-0 shadow-md transition-opacity duration-150 group-hover:opacity-100 group-focus-within:opacity-100 sm:left-1/2 sm:-translate-x-1/2">{children}</span></span>
}
