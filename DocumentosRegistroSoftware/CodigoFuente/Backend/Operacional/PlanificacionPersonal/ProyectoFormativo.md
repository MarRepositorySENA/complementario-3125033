```
//ENTITY PROYECTOFORMATIVO
package com.persona.Backend.Entity.Operational.PlanificacionFormativa;

import com.persona.Backend.Entity.BaseEntity;
import com.persona.Backend.Entity.Parameter.Infraestrutura.CentroFormacion;

import jakarta.persistence.Column;
import jakarta.persistence.Entity;
import jakarta.persistence.FetchType;
import jakarta.persistence.JoinColumn;
import jakarta.persistence.OneToOne;
import jakarta.persistence.Table;

@Entity
@Table(name = "proyecto_formativo")
public class ProyectoFormativo extends BaseEntity {

	@Column(name = "titulo", length = 45, nullable = false)
	private String titulo;

	@Column(name = "codigo", length = 45, nullable = false)
	private String codigo;

	@Column(name = "descripcion", length = 100, nullable = false)
	private String descripcion;

	@Column(name = "cantidad_rap", nullable = false)
	private Integer cantidadRap;

	@OneToOne(fetch = FetchType.EAGER, optional = false)
	@JoinColumn(name = "centro_formacion_id", nullable = false, unique = false)
	private CentroFormacion centroFormacionId;

	public String getTitulo() {
		return titulo;
	}

	public void setTitulo(String titulo) {
		this.titulo = titulo;
	}

	public String getCodigo() {
		return codigo;
	}

	public void setCodigo(String codigo) {
		this.codigo = codigo;
	}

	public String getDescripcion() {
		return descripcion;
	}

	public void setDescripcion(String descripcion) {
		this.descripcion = descripcion;
	}

	public Integer getCantidadRap() {
		return cantidadRap;
	}

	public void setCantidadRap(Integer cantidadRap) {
		this.cantidadRap = cantidadRap;
	}

	public CentroFormacion getCentroFormacionId() {
		return centroFormacionId;
	}

	public void setCentroFormacionId(CentroFormacion centroFormacionId) {
		this.centroFormacionId = centroFormacionId;
	}

}
//IREPOSITORY PROYECTOFORMATIVO
package com.persona.Backend.IRepository.Operational.PlanificacionFormativa;

import org.springframework.stereotype.Repository;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ProyectoFormativo;
import com.persona.Backend.IRepository.IBaseRepository;

@Repository
public interface IProyectoFormativoRepository extends IBaseRepository<ProyectoFormativo, Long> {

}

//ISERVICE PROYECTOFORMATIVO
package com.persona.Backend.IService.Operational.PlanificacionFormativa;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ProyectoFormativo;
import com.persona.Backend.IService.IBaseService;

public interface IProyectoFormativoService extends IBaseService<ProyectoFormativo>{

}

//SERVICE PROYECTOFORMATIVO
package com.persona.Backend.Service.Operational.PlanificacionFormativa;

import org.springframework.stereotype.Service;

import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ProyectoFormativo;
import com.persona.Backend.IService.Operational.PlanificacionFormativa.IProyectoFormativoService;
import com.persona.Backend.Service.BaseService;

@Service
public class ProyectoFormativoService extends BaseService<ProyectoFormativo> implements IProyectoFormativoService {

}

//CONTROLLER PROYECTOFORMATIVO
package com.persona.Backend.Controller.Operational.PlanificacionFormativa;

import org.springframework.web.bind.annotation.CrossOrigin;
import org.springframework.web.bind.annotation.RequestMapping;
import org.springframework.web.bind.annotation.RestController;

import com.persona.Backend.Controller.BaseController;
import com.persona.Backend.Entity.Operational.PlanificacionFormativa.ProyectoFormativo;

@CrossOrigin("*")
@RestController
@RequestMapping("/api/v1/base/operational/planificacion_formativa/proyecto_formativo")
public class ProyectoFormativoController extends BaseController<ProyectoFormativo>{

}

```